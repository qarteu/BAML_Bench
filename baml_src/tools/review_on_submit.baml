class ReviewOnSubmitResult {
    review_comments string[] @description("list of review comments and suggestions")
    status string @description("status of the review")
    files_reviewed string[] @description("list of files that were reviewed")
}

function ReviewOnSubmit(user_message: string) -> ReviewOnSubmitResult {
    client "openai/gpt-4"
    prompt #"
        Review the changes for submission based on the user message.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "review_comments": ["list of review comments"],
            "status": "status of the review",
            "files_reviewed": ["list of files reviewed"]
        }
    "#
} 