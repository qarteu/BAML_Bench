from baml_client import b   
from baml_client.types import EditRewrite, FindFileResult, SearchDirResult, SearchFileResult, SubmitResult, ReviewOnSubmitResult, EditLintingResult
import os

def test_edit():
    edit_info = b.EditFile("Update the README.md to add installation instructions")
    print("\nEdit Test Results:")
    # Keep the assertion to verify type
    assert isinstance(edit_info, EditRewrite)
    print(f"Changes to make: {edit_info.text}")
    print(f"File to modify: {edit_info.modified_path}")

def test_search():
    #test find_file
    find_result = b.FindFile("Find all Python files in src/")
    print("\nFind File Results:")
    assert isinstance(find_result, FindFileResult)
    print(f"Looking for: {find_result.file_name}")
    print(f"In directory: {find_result.dir}")
    print("Matches:", find_result.matches)

    #test search_dir
    dir_result = b.SearchDir("Find TODO comments in the project")
    print("\nSearch Directory Results:")
    assert isinstance(dir_result, SearchDirResult)
    print(f"Searching for: {dir_result.search_term}")
    print(f"In directory: {dir_result.dir}")
    print("Matches:", dir_result.matches)

    # Test search_file
    file_result = b.SearchFile("Find function definitions in main.py")
    print("\nSearch File Results:")
    assert isinstance(file_result, SearchFileResult)
    print(f"Searching for: {file_result.search_term}")
    print(f"In file: {file_result.file}")
    print("Matches:", file_result.matches)

def test_submit():
    submit_info = b.Submit("Submit the current changes")
    print("\nSubmit Test Results:")
    assert isinstance(submit_info, SubmitResult)
    print(f"Status: {submit_info.status}")

def test_review_on_submit():
    review_info = b.ReviewOnSubmit("Review my changes before submission")
    print("\nReview On Submit Test Results:")
    assert isinstance(review_info, ReviewOnSubmitResult)
    print(f"Status: {review_info.status}")
    print("Review Comments:", review_info.review_comments)
    print("Files Reviewed:", review_info.files_reviewed)

def test_edit_linting():
    lint_info = b.EditLinting("Fix indentation in lines 5-10")
    print("\nEdit Linting Test Results:")
    assert isinstance(lint_info, EditLintingResult)
    print(f"Start line: {lint_info.start_line}")
    print(f"End line: {lint_info.end_line}")
    print(f"Replacement text: {lint_info.replacement_text}")

def main():
    #API key verification
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    #tst all tools
    test_edit()
    test_search()
    test_submit()
    test_review_on_submit()
    test_edit_linting()


if __name__ == '__main__':
    main()