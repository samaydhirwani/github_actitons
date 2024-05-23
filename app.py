import streamlit as st

def main(): 

    # Get the height of the browser window
    browser_height = st.query_params.get('height', [600])[0]

    # Calculate the height for each HTML component
    html_height = int(browser_height)   # Adjusted for headers and margins

    with open("chat_6.html", "r",encoding='utf-8') as f:
        html_content = f.read()

# Read the content of the JavaScript file
    with open("chat_6.js", "r",encoding='utf-8') as f:
        js_content = f.read()

# Read the content of the CSS file
    with open("styles_7.css", "r") as f:
        css_content = f.read()

# Combine HTML, JavaScript, and CSS content
    combined_content = f"""
    <style>{css_content}</style>
    <script>{js_content}</script>
    {html_content}
"""
    


    # Add content to each column

        #st.header("Column 1")
    st.components.v1.html(combined_content, width=1000, height=html_height,scrolling=False)

    

if __name__ == "__main__":
    main()





