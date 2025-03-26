class FindFileResult {
    file_name string @description("the name of the file or pattern to search for. supports shell-style wildcards (e.g. *.py)")
    dir string? @description("the directory to search in (if not provided, searches in the current directory)")
    matches string[] @description("list of matching files found")
}

class SearchDirResult {
    search_term string @description("the term to search for")
    dir string? @description("the directory to search in (if not provided, searches in the current directory)")
    matches string[] @description("list of matches found in directory")
}

class SearchFileResult {
    search_term string @description("the term to search for")
    file string? @description("the file to search in (if not provided, searches in the current open file)")
    matches string[] @description("list of matches found in file")
}

function FindFile(user_message: string) -> FindFileResult {
    client "openai/gpt-4"
    prompt #"
        Extract file search parameters from the user message.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "file_name": "pattern to search for (e.g. *.py)",
            "dir": "optional directory to search in",
            "matches": ["list of matching files"]
        }
    "#
}

function SearchDir(user_message: string) -> SearchDirResult {
    client "openai/gpt-4"
    prompt #"
        Extract directory search parameters from the user message.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "search_term": "term to search for",
            "dir": "optional directory to search in",
            "matches": ["list of matches found"]
        }
    "#
}

function SearchFile(user_message: string) -> SearchFileResult {
    client "openai/gpt-4"
    prompt #"
        Extract file search parameters from the user message.
        User message: {{user_message}}
        
        You must return a JSON object with these exact fields:
        {
            "search_term": "term to search for",
            "file": "optional file to search in",
            "matches": ["list of matches found"]
        }
    "#
}