from abc import ABC, abstractmethod
import gradio as gr


class BaseTab(ABC):
    @abstractmethod
    def create_inner_tab(self) -> gr.Blocks:
        raise NotImplementedError()

    def _get_tab_header(self) -> gr.Markdown:
        return gr.Markdown(f"""
        # Bio
        Create your speaker bio 🤓
        """)

    def create(self) -> gr.Blocks:
        tab = self.create_inner_tab()
        # t .blocks.insert(0, self._get_tab_header())
        return tab