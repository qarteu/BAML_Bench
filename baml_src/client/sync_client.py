from baml import BamlClient

class SWEBamlClient:
    def __init__(self):
        self.client = BamlClient()
        self.tools = self.client.load_tools("baml_src/tools")
    
    def edit_rewrite(self, text: str) -> str:
        return self.client.EditRewrite(text=text)