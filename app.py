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

    
    st.subheader('Neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeel')
    
    st.markdown('A very Happy Birthday!!!!', unsafe_allow_html=True)
    st.image('words.png')
    

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

    st.subheader('Tuku, the parrot !!')
    st.markdown("It's Tuku here again, though we already got introduced on the home page, I talk a lot, don't I,👻, So, this was a small gift from me, I don't know when you will start writing poems again, given your tight schedule. But I really hope, you start wriitng again, just because you are an extremely talented writer, and may be this token of gift reminds you of that. That's all, won't talk much 😉",unsafe_allow_html=True)
    
