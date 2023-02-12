import pandas as pd
import streamlit as st
import random, time
from pages.Courses import ds_course,uiux_course,sde,devops,python_developer,resume_videos,interview_videos
import streamlit.components.v1 as com
from streamlit_tags import st_tags


def course_recommender(course_list):
    st.subheader("**Courses & Certificates Recommendations**")
    c = 0
    rec_course = []
    # no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 4)
    random.shuffle(course_list)
    for c_name, c_link in course_list:
        c += 1
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)

    return rec_course

st.subheader("**Skills Recommendation💡**")

st.title('Resource Sharing')

if st.button('Data Analyst'):
    recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining','Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping','ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
    recommended_keywords = st_tags(label='### Recommended skills.',
    text='Recommended skills generated from System',value=recommended_skills,key = '1')
    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
    rec_course = course_recommender(ds_course)
    st.button('Python Developer')
    st.button('Software Developer')
    st.button('DevOps')
    st.button('UI/ UX Designer')
    time.sleep(20)

elif st.button('UI/ UX Designer'):
    recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
    recommended_keywords = st_tags(label='### Recommended skills for you.',
    text='Recommended skills generated from System',value=recommended_skills,key = '5')
    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
    rec_course = course_recommender(uiux_course)
    st.button('Data Analyst')
    st.button('Python Developer')
    st.button('Software Developer')
    st.button('DevOps')
    time.sleep(10)

elif st.button('DevOps'):
    recommended_skills = ['Continuous Integration ','Docker','Java', 'Javascript', 'Ruby','Shell','Bash','PHP','Automation',' Cloud','Linux Fundamentals','Scripting Skills']
    recommended_keywords = st_tags(label='### Recommended skills for you.',
    text='Recommended skills generated from System',value=recommended_skills,key = '4')
    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
    rec_course = course_recommender(devops)

    st.button('Data Analyst')
    st.button('Python Developer')
    st.button('Software Developer')
    st.button('UI/ UX Designer')
    time.sleep(10)

elif st.button('Python Developer'):
    recommended_skills=['Django','Amazon Web Services (AWS)',' APIs',' Docker',' Linux ','Cloud Computing',' Machine Learning',' Git', 'Continuous','Integration',' React ','Flask',' REST ','PostgreSQL ','DevOps ','Microservices ','JavaScript','Java','SQL','Go']
    recommended_keywords = st_tags(label='### Recommended skills for you.',
    text='Recommended skills generated from System',value=recommended_skills,key = '2')
    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
    rec_course = course_recommender(python_developer)

    st.button('Data Analyst')
    st.button('Software Developer')
    st.button('UI/ UX Designer')
    st.button('DevOps')
    time.sleep(10)

elif st.button('Software Devloper'):
    recommended_skills = [' SQL','Docker','Kubernetes','Cloud Computing','Data Structures & Algorithms','Java','Python','C#/.Net','Mean','Ruby','Software Testing and Debugging','Object-Oriented Design (OOD)','Linux (UNIX)','Scripting','Analytical Skills','Solving']
    recommended_keywords = st_tags(label='### Recommended skills for you.',
    text='Recommended skills generated from System',value=recommended_skills,key = '3')
    st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
    rec_course = course_recommender(sde)
    st.button('Data Analyst')
    st.button('Python Developer')
    st.button('Software Developer')
    st.button('DevOps')
    st.button('UI/ UX Designer')
    time.sleep(10)


# Resume writing video
st.header("**Bonus Video for Resume Writing Tips💡**")
resume_vid = random.choice(resume_videos)
st.video(resume_vid)

## Interview Preparation Video
st.header("**Bonus Video for Interview👨‍💼 Tips💡**")
interview_vid = random.choice(interview_videos)
st.video(interview_vid)

# com.html("""<iframe width="996" height="560" src="https://www.youtube.com/embed/hqu5EYMLCUw" title="Resume Analyser Application using NLP Python with Code | Full Responsive Web Application" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>""")
