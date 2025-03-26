class EditRewrite {
    text string @description("The text to replace the currently displayed lines with")
    modified_path string @description("Path to the modified file")
}

function EditFile(user_message: string) -> EditRewrite {
    client "openai/gpt-4"
    prompt #"
        Extract the file changes from the user message and return them in a structured format.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "text": "the changes to make",
            "modified_path": "the path to the file"
        }
    "#
}