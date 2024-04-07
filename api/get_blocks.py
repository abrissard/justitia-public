from typing import List, Tuple
import dataclasses
import datetime
import itertools
import numpy as np
import openai
import regex as re
import requests
import time

# ---------------------------------- constants ---------------------------------

EMBEDDING_MODEL = "text-embedding-ada-002"

# ------------------------------------ types -----------------------------------

@dataclasses.dataclass
class Block:
    title: str
    text: str
    
# ------------------------------------------------------------------------------

# Get the embedding for a given text. The function will retry with exponential backoff if the API rate limit is reached, up to 4 times.
def get_embedding(text: str) -> np.ndarray:

    max_retries = 4
    max_wait_time = 10
    attempt = 0

    while True:
        try:
            result = openai.Embedding.create(model=EMBEDDING_MODEL, input=text)
            return result["data"][0]["embedding"]

        except openai.error.RateLimitError as e:

            attempt += 1

            if attempt > max_retries: raise e

            time.sleep(min(max_wait_time, 2 ** attempt))


# Get the k blocks most semantically similar to the query using Pinecone.
def get_top_k_blocks(index, user_query: str, k: int) -> List[Block]:

    # Default to querying embeddings from live website if pinecone url not
    # present in .env
    #
    # This helps people getting started developing or messing around with the
    # site, since setting up a vector DB with the embeddings is by far the
    # hardest part for those not already on the team.

    # print time
    t = time.time()

    # Get the embedding for the query.
    query_embedding = get_embedding(user_query)

    t1 = time.time()
    print("Time to get embedding: ", t1 - t)

    query_response = index.query(
        namespace="ns1",
        top_k=k,
        include_values=False,
        include_metadata=True,
        vector=query_embedding
    )
    blocks = []
    for match in query_response['matches']:

        # date = match['metadata']['date']

        # if type(date) == datetime.date: date = date.strftime("%Y-%m-%d") # iso8601

        blocks.append(Block(
            title = match['metadata']['title'],
            # author = match['metadata']['author'],
            # date = date,
            # url = match['metadata']['url'],
            # tags = match['metadata']['tags'],
            text = strip_block(match['metadata']['text'])
        ))

    t2 = time.time()

    print(f"Time to get top-{k} blocks: ", t2 - t1)
    print("Blocks: ", blocks)
    
    # remove duplicates from blocks
    blocks = list({block.title: block for block in blocks}.values())

    return blocks


# we add the title and authors inside the contents of the block, so that
# searches for the title or author will be more likely to pull it up. This
# strips it back out.
def strip_block(text: str) -> str:
    r = re.match(r"^\"(.*)\"\s*-\s*Title:.*$", text, re.DOTALL)
    if not r:
        print("Warning: couldn't strip block")
        print(text)
    return r.group(1) if r else text
