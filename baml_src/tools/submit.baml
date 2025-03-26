class SubmitResult {
    status string @description("status of the submission")
}

function Submit(user_message: string) -> SubmitResult {
    client "openai/gpt-4"
    prompt #"
        Process the submission request.
        User message: {{user_message}}
        
        You must return a JSON object with:
        {
            "status": "status of the submission"
        }
    "#
}