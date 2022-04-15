import streamlit as st
from main import *
import base64

st.balloons()

st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Menu </h1>',
                    unsafe_allow_html=True)
option = st.sidebar.radio(" ",('Home', 'Manage Your Poems','About Me'))

if option == 'Home':
    
    # LOGO_IMAGE = "omdena_india_logo.png"
    
    st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .logo-text {
             font-weight:700 !important;
             font-size:50px !important;
             color: #f9a01b !important;
             padding-top: 75px !important;
        }
        .logo-img {
             float:right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # st.markdown(
    #       f"""
    #       <div class="container">
    #            <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
    #       </div>
    #       """,
    #       unsafe_allow_html=True
    # )
    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        body {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

    set_png_as_page_bg('cats.jpeg')
    st.subheader('OWLS')
    
    st.markdown('Happy Birthday', unsafe_allow_html=True)
    st.markdown("Hey, it's me again So, it's your birthday and I know you know, you don't like birthday gifts, but trust me, this is just a very tiny token of gift from me I know, it's not the only way to show my affection for you, but one of the ways, may be. Well, to say you are with no doubt one of the important persons in my life. You mean so much to me. You know, you are sweet in your own way, I know you sometimes like to make new friends, meet new people, share your knowledge, and that is totally fine, you know. You would anyway share your knowledge 😂, and you are a great person. You are achieving great heights and may you achieve more. You are an absolutely humorous person, your jokes on any part of the house or insects, animals make me laugh so hard, it literally makes my day. You are very cute when you get angry or annoyed. I am finally at peace, that we are finally in a happy space. I don't know how much you are happy with me but I am like real happy with you. You are a very very kind, humble and down to earth person. That's the most amazing trait about you. I know we will have may be many problems coming up but we will always fight them and solve them together.",unsafe_allow_html=True)

elif option == 'Manage Your Poems':

    st.subheader('SELECT OPERATION')    
    
    col1, col2 = st.columns(2)

    opr_type = col1.selectbox("List of Operations",("getPoem", "post", "patch","delete"))
    with col1:
        nameOfThePoem = st.text_input('Type Poem Name')
    #     getPoem = st.text_input('Get Poem Content')
    #     post = st.text_input('Create Poem Content')
    # with col2:
    #     patch = st.text_input('Update Poem Content')
    #     delete = st.text_input('Delete Poem Content')


    


    if opr_type == 'post':
            data_file = st.file_uploader("Upload poem",type=["txt"])
            if data_file is not None:
                if data_file.type == "text/plain":
                    new_dict = dict()
                    for i,line in enumerate(data_file):
                        if '\\n' not in str(line):
                            line = str(line)[:-1] + "\\n'"
                        line = str(line).replace("b'", "")
                        line = str(line).replace("\\n'","")
                        new_dict['Line no.'+str(i)] = line
                        
                    if st.button('Submit'):
                        create(nameOfThePoem, new_dict)
                        st.text('Created')
                    new_dict = dict()
            else:
                st.text("Please upload a text file!!")
            
                
    elif opr_type == 'patch':
        data_file = st.file_uploader("Upload poem",type=["txt"])
        if data_file is not None:
            # file_details = {"filename":data_file.name, "filetype":data_file.type,
            #                 "filesize":data_file.size}
            # st.write(file_details)

            if data_file.type == "text/plain":
                new_dict = dict()
                for i,line in enumerate(data_file):
                    if '\\n' not in str(line):
                        line = str(line)[:-1] + "\\n'"
                    line = str(line).replace("b'", "")
                    line = str(line).replace("\\n'","")
                    new_dict['Line no.'+str(i)] = line
                    st.text(line)
            prev = {'PoemName': nameOfThePoem}  
            new = {"$set": {'Content': new_dict}}
            if st.button('Submit'):
                if GetPoemName(prev) is not None:
                    update(prev, new)
                    st.text('Updated')
                else:
                    st.text("Available Poems: ")
                    for name in getAll():
                        st.text(name)
                new_dict = dict()
                
            
        else:
            st.text("Please upload a text file!!")
        
    elif opr_type == 'getPoem':
        if st.button('Submit'):
            # if GetPoem(nameOfThePoem)is None:
            if nameOfThePoem not in getAll():
                st.text("Available Poems: ")
                for name in getAll():
                    st.text(name)
            else:
                for value in GetPoem(nameOfThePoem).values():
                    st.text(value)
    elif opr_type == 'delete':
        if st.button('Submit'):
            # if GetPoemName(nameOfThePoem) is not None:
            #     delete(nameOfThePoem)
            #     st.text('Deleted')
            if nameOfThePoem in getAll():
                delete({"PoemName": nameOfThePoem})
                st.text('Deleted')

            else:
                st.text("Available Poems: ")
                for name in getAll():
                    st.text(name)

        
            


elif option == 'About Me':

    st.subheader('Tuku')
    
