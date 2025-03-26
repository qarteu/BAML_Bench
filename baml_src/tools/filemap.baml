class FileMapResult {
    file_path string @description("The path to the file to be read")
    content string @description("The processed content of the file, with lengthy functions skipped")
}

function FileMap(user_message: string) -> FileMapResult {
    client "openai/gpt-4"
    prompt #"
        Extract the file path from the user message and process the file content.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "file_path": "path to the file to read",
            "content": "processed content of the file, skipping lengthy functions"
        }
        
        Note: The content should be processed to skip lengthy function and method definitions
        while preserving the overall structure of the file.
    "#
} 