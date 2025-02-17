{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0848edb4-0498-4aa8-a5fc-014d4e8ce33c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# py ai code review"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f12f1577-fe06-4739-9aec-2b3333bfe3e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: google-generativeai in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (0.8.4)\n",
      "Requirement already satisfied: google-ai-generativelanguage==0.6.15 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-generativeai) (0.6.15)\n",
      "Requirement already satisfied: google-api-core in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-generativeai) (2.24.1)\n",
      "Requirement already satisfied: google-api-python-client in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-generativeai) (2.161.0)\n",
      "Requirement already satisfied: google-auth>=2.15.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-generativeai) (2.38.0)\n",
      "Requirement already satisfied: protobuf in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-generativeai) (5.29.3)\n",
      "Requirement already satisfied: pydantic in c:\\programdata\\anaconda3\\lib\\site-packages (from google-generativeai) (2.8.2)\n",
      "Requirement already satisfied: tqdm in c:\\programdata\\anaconda3\\lib\\site-packages (from google-generativeai) (4.66.5)\n",
      "Requirement already satisfied: typing-extensions in c:\\programdata\\anaconda3\\lib\\site-packages (from google-generativeai) (4.11.0)\n",
      "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-ai-generativelanguage==0.6.15->google-generativeai) (1.26.0)\n",
      "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-core->google-generativeai) (1.67.0)\n",
      "Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from google-api-core->google-generativeai) (2.32.3)\n",
      "Requirement already satisfied: cachetools<6.0,>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from google-auth>=2.15.0->google-generativeai) (5.3.3)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from google-auth>=2.15.0->google-generativeai) (0.2.8)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-auth>=2.15.0->google-generativeai) (4.9)\n",
      "Requirement already satisfied: httplib2<1.dev0,>=0.19.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-python-client->google-generativeai) (0.22.0)\n",
      "Requirement already satisfied: google-auth-httplib2<1.0.0,>=0.2.0 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-python-client->google-generativeai) (0.2.0)\n",
      "Requirement already satisfied: uritemplate<5,>=3.0.1 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-python-client->google-generativeai) (4.1.1)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from pydantic->google-generativeai) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pydantic->google-generativeai) (2.20.1)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from tqdm->google-generativeai) (0.4.6)\n",
      "Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.70.0)\n",
      "Requirement already satisfied: grpcio-status<2.0.dev0,>=1.33.2 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai) (1.70.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from httplib2<1.dev0,>=0.19.0->google-api-python-client->google-generativeai) (3.1.2)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\programdata\\anaconda3\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth>=2.15.0->google-generativeai) (0.4.8)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (2024.12.14)\n"
     ]
    }
   ],
   "source": [
    "!pip install google-generativeai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "779aa387-28cb-4b0f-845b-b4e99ae826ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "import google.generativeai as genai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b383816c-89aa-44f6-9327-517d6c46fb6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: streamlit in c:\\programdata\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\home\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (5.29.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\programdata\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.12.14)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "22e47ee5-2adc-4308-b13c-9ff931d11f5b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import google.generativeai as genai\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5d0c0d78-00c3-45b5-b080-0b50695b4623",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(\n",
    "    page_title=\"AI Code Reviewer\",\n",
    "    page_icon=\"✨\",\n",
    "    layout=\"wide\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5a7c3ac6-b31b-47d5-aaa2-cc1b585aac51",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-17 19:11:28.134 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "api_key = os.getenv(\"AIzaSyBVOM4Pct30jaUcFUiXpbMy4hVOv2f3kKk\")\n",
    "if not api_key:\n",
    "    st.error(\"API key not found. Please set GENAI_API_KEY in the environment.\")\n",
    "    st.stop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "40cd71df-f40a-4560-920e-bd4ecbdd7f7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "genai.configure(api_key=api_key)\n",
    "model = genai.GenerativeModel(\"gemini-pro\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "4e1cb3bf-df31-4738-bc3a-508aa0170c57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"<h1 style='text-align: center;'>AI Code Reviewer</h1>\", unsafe_allow_html=True)\n",
    "st.markdown(\"<h4 style='text-align: center; color: gray;'>Analyze and optimize your Python code effortlessly</h4>\", unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a3b4091f-86b8-4402-a93c-c96c64d28104",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-17 19:12:45.142 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "col1, col2 = st.columns([3, 2])\n",
    "\n",
    "with col1:\n",
    "    st.markdown(\"### Paste Your Python Code Here:\")\n",
    "    code_input = st.text_area(\"Enter your Python code\", height=300, label_visibility=\"collapsed\")\n",
    "\n",
    "with col2:\n",
    "    st.markdown(\"### AI Code Review Output:\")\n",
    "    review_output = st.empty()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "643be00b-f379-4b49-b78f-229cfca43f8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def review_code(code):\n",
    "    \"\"\"Generates a detailed review of the provided Python code using Google Gemini AI.\"\"\"\n",
    "    prompt = f\"\"\"\n",
    "    Analyze the following Python code and identify:\n",
    "    \n",
    "    1. Code functionality\n",
    "    2. Errors and issues\n",
    "    3. Performance improvements\n",
    "    4. Readability and maintainability enhancements\n",
    "    5. Final rating out of 5\n",
    "    \n",
    "    Code:\n",
    "    {code}\n",
    "    \"\"\"\n",
    "    try:\n",
    "        response = model.generate_content(prompt)\n",
    "        return response.text\n",
    "    except Exception as e:\n",
    "        return f\"Error processing request: {str(e)}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7c016130-7beb-4d24-beea-98852251454a",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.markdown(\"---\")\n",
    "center_button = st.columns([2, 1, 2])[1]\n",
    "with center_button:\n",
    "    if st.button(\"🔍 Review Code\", use_container_width=True):\n",
    "        if code_input.strip():\n",
    "            with st.spinner(\"Reviewing your code... Please wait.\"):\n",
    "                review_result = review_code(code_input)\n",
    "                review_output.write(review_result)\n",
    "        else:\n",
    "            st.warning(\"Please enter a Python code snippet.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "f8a9bd82-7f5b-4ce4-9731-2676b35d62f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.sidebar.title(\"📌 How to Use\")\n",
    "st.sidebar.info(\"\"\"\n",
    "1. Paste your Python code in the input box.\n",
    "2. Click the 'Review Code' button.\n",
    "3. AI will analyze and provide feedback.\n",
    "4. Use suggestions to optimize your code.\n",
    "\"\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "4b37e814-8449-4a6d-9cf5-9792378dc59a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=1, _parent=DeltaGenerator())"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.sidebar.markdown(\"---\")\n",
    "st.sidebar.markdown(\"💡 **Powered by Google Gemini AI**\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "5945ca49-6705-4e65-9c50-dc3bbffe9c4f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"<hr>\", unsafe_allow_html=True)\n",
    "st.markdown(\"<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit & Gemini AI</p>\", unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0d4f8178-1aaf-4e0d-9cc5-c6df9cdb8dae",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
