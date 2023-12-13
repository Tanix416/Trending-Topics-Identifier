import gradio as gr
import subprocess


def process_input(keyword, country_region=""):

  output_string = f"Keyword: {keyword}"
  if country_region:
    output_string += f" - Country/Region: {country_region}"

  with open("submitted_Keyword.txt","w") as f:
    f.write(keyword)
  with open("submitted_Region.txt","w") as f:
    f.write(country_region)

  # Run the Python file
  subprocess.run(["python", "run_ipynb.py"])

  # Read topic information from file
  with open("post.txt", "r",encoding="utf-8") as f:
    topics = f.read().strip()

  # Append topic information to the output string
  output_string += f"\n\nTopics: {topics}"
  return output_string


# Create the Gradio interface with background color
interface = gr.Interface(
    fn=process_input,
    inputs=["text", gr.Textbox(placeholder="Country/Region (optional)")],
    outputs="text",
    title="Keyword Processor",
    description="Enter a keyword and optionally a country/region to see the output.",
)

# Launch the interface
interface.launch(inline=True,inbrowser=True,debug=True,show_error=True)