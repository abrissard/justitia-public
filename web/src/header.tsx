import React from "react";
import Link from "next/link";

const Header: React.FC<{page: "index" | "semantic"}> = ({page}) => {
    const sidebar = page === "index" ? (
        <span className="flex flex-col font-semibold flex-1 justify-start text-right">
            <p className="my-0">Conversational Agent</p>
            <Link href="/semantic">Semantic Search</Link>
        </span>
    ) : (
        <span className="flex flex-col font-semibold flex-1 justify-start text-right">
            <Link href="/">Conversational Agent</Link>
            <p className="my-0">Semantic Search</p>
        </span>
    );
        
    return (
        <>
            <div className="flex my-4">
                <h1 className="flex-1 my-0">JustitIA</h1>
            </div>
            <p>
                Welcome to JustitIA, your legal chatbot companion :)
            </p>
            <p>
                Whether you are curious about what and where your data is stored by a product/ service you use or need clarification on specific legal terms, justitIA is here to help.
            </p>
            <p>
                With JustitIA, you can quickly and easily access information about the legal aspects of various products and services. Our chatbot is equipped to provide clear explanations and guidance on a wide range of topics, including terms of service, privacy policies, and user rights.
            </p>
            <div>
                <h2 className="flex-1 my-0">NOTE:</h2>
            </div>
            <p>
                We are committed to protecting your privacy. Please note that JustitIA won't be storing any of your personal information, so you can interact confidently!
            </p>
            <div>
                <h2 className="flex-1 my-0">Curious about how JustitIA answers your questions?</h2>
                <p>
                    Justitia is a chatbot using RAG. RAG stands for Retrieval Augmented Generation and it means that the chatbot uses documents from a knowledge base to answer your questions more accurately and to provide sources.
                </p>
                <p>
                    For more information about how RAG works in details you can read this great article: <a href="https://www.pinecone.io/learn/retrieval-augmented-generation/">What is retrieval augmented generation (RAG)?</a>.
                    We used Pinecone for our vector database and gpt-3.5-turbo for our generation model. The company documents are from a public dataset and were captured around 2021.
                </p>
            </div>
            <p>
                We hope that it can be a useful tool for the community, and we're eager to hear feedback and suggestions. If you are not satisfied with the answer, please consult the original company's documents or contact their legal department.
            </p>
        </>
    );
};

export default Header;
