# AI-Workflow
Basically trying to recreate Stack-AI's Workflow product

## Components in their Workflow

- User Input: An input field where the user will enter an query regarding the documents.

- Documents + Search: An input field where the user can upload an document.

- Model: An dropdown field where the user can select which models to use, currently I want to do for just huggingface models, the user will give the model-id (example: microsoft/phi-2)

- Output: Basically the output regarding the user's query.

## UI

Creating UI using vercel's vO and then using python in backend to create apis. This whole thing will be like a canvas where the user can move the individual components (Input, Docs + Search, Model, Output) and a run button which will bascially run the workflow.

## Psuedo Steps:

- The user will enter an query.
- The user will upload an document(PDFs, CSVs as of now).
- The user will pass the model's name.
- The user will click on the run button.
- The user will see the output.