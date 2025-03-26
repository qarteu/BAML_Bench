class EditAnthropicResult {
    command string @description("The command to run (view, create, str_replace, insert, undo_edit)")
    path string @description("Absolute path to file or directory")
    file_text string? @description("Content for file creation")
    old_str string? @description("String to replace in str_replace command")
    new_str string? @description("New string for replacement or insertion")
    insert_line int? @description("Line number for insertion")
    view_range int[]? @description("Line range for viewing file")
}

function EditAnthropic(user_message: string) -> EditAnthropicResult {
    client "openai/gpt-4"
    prompt #"
        Extract the edit parameters from the user message for Anthropic-style editing.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "command": "one of: view, create, str_replace, insert, undo_edit",
            "path": "absolute path to file or directory",
            "file_text": "optional content for file creation",
            "old_str": "optional string to replace",
            "new_str": "optional new string for replacement/insertion",
            "insert_line": "optional line number for insertion",
            "view_range": "optional array of [start_line, end_line] for viewing"
        }
        
        Note: 
        - For str_replace: old_str must match exactly one or more consecutive lines
        - For insert: new_str and insert_line are required
        - For view: view_range is optional, [start_line, -1] shows from start to end
        - For create: file_text is required
    "#
} 