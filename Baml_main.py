from baml_client import b   
from baml_client.types import EditRewrite
import os
def main():
    
    # Verify key is loaded
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    edit_info = b.EditFile("Update the README.md to add installation instructions")
    print(edit_info)
    assert isinstance(edit_info, EditRewrite)
    print(f"Changes to make: {edit_info.text}")
    print(f"File to modify: {edit_info.modified_path}")

if __name__ == '__main__':
    main()