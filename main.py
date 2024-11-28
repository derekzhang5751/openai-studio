import gradio as gr


from pages.image_reader import image_reader_page

if __name__ == "__main__":
    home_page = gr.TabbedInterface(
        [image_reader_page],
        ["Image Reader"]
    )
    home_page.launch(share=False)
    pass
