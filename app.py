import gradio as gr

from rag import create_vectorstore, search
from llm import generate_answer


vectorstore = None


def process_pdf(pdf):

    global vectorstore

    vectorstore = create_vectorstore(pdf.name)

    return "✅ PDF Loaded Successfully!"


def ask_question(question):

    global vectorstore

    if vectorstore is None:
        return "Please upload a PDF first."

    context = search(vectorstore, question)

    answer = generate_answer(question, context)

    return answer


with gr.Blocks(title="DocuMind") as demo:

    gr.Markdown(
        """
# 📄 DocuMind

### Chat with any PDF using AI
"""
    )

    pdf = gr.File(
        label="Upload PDF",
        file_types=[".pdf"]
    )

    upload_btn = gr.Button("Load PDF")

    status = gr.Textbox(
        label="Status"
    )

    question = gr.Textbox(
        label="Ask a Question"
    )

    ask_btn = gr.Button("Ask")

    answer = gr.Textbox(
        label="Answer",
        lines=10
    )

    upload_btn.click(
        process_pdf,
        inputs=pdf,
        outputs=status
    )

    ask_btn.click(
        ask_question,
        inputs=question,
        outputs=answer
    )


demo.launch()