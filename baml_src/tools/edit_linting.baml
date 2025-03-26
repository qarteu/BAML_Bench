class EditLintingResult {
    start_line int @description("the line number to start the edit at")
    end_line int @description("the line number to end the edit at (inclusive)")
    replacement_text string @description("the text to replace the current selection with")
}

function EditLinting(user_message: string) -> EditLintingResult {
    client "openai/gpt-4"
    prompt #"
        Extract the edit parameters from the user message for linting.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "start_line": "line number to start edit",
            "end_line": "line number to end edit",
            "replacement_text": "text to replace with (including proper indentation)"
        }
        
        Note: The replacement text must maintain proper indentation.
        For example, if adding 'print(x)', include all necessary spaces before the code.
    "#
} 