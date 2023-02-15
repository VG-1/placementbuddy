import streamlit as st
import pandas as pd
import streamlit.components.v1 as com
# com.html("""

# <div>
# <h1>
# <div class="iframely-embed">
# <div class="iframely-responsive" style="padding-bottom: 52.5%; padding-top: 120px;"><a href="https://roadmap.sh/frontend" data-iframely-url="//iframely.net/XJ5xa8M"></a></div></div><script async src="//iframely.net/embed.js"></script>
# </h1>
# dddhdj
# <div>
# <h1>
# <div class="iframely-embed">
# <div class="iframely-responsive" style="padding-bottom: 52.5%; padding-top: 120px;"><a href="https://roadmap.sh/backend" data-iframely-url="//iframely.net/XJ5xa8M"></a></div></div><script async src="//iframely.net/embed.js"></script>
# </h1>

# </div>

# """)

st.header('We are here to help you throughout the placement procedure')
st.subheader('Please find all the resources and roadmaps here :)')
url = 'https://roadmap.sh/pdfs/roadmaps/frontend.pdf'

st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">Front-end Roadmap</button></a>''',
unsafe_allow_html=True)
url = 'https://roadmap.sh/pdfs/roadmaps/backend.pdf'

st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">Back-end Roadmap</button></a>''',
unsafe_allow_html=True)
url = 'https://roadmap.sh/pdfs/roadmaps/devops.pdf'

st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">DevOps Roadmap</button></a>''',
unsafe_allow_html=True)
url = 'https://roadmap.sh/pdfs/roadmaps/blockchain.pdf'

st.markdown(f'''<a href={url}><button style="background-color:GreenYellow;">Blockchain Roadmap</button></a>''',unsafe_allow_html=True)

# com.html("""<iframe  src="https://www.youtube.com/embed/nFQ22Wb6Qe8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></h1>""")
# com.html("""<iframe   src="https://www.youtube.com/embed/nFQ22Wb6Qe8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></h1>""")
# com.html("""<div style="left: 0; width: 100%; height: 600px; position: relative;"><iframe src="https://9bw5lmx29ue.typeform.com/to/NljNEayv?typeform-embed=oembed&typeform-medium=embed-oembed&format=json&disable-auto-focus=true" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen allow="encrypted-media;"></iframe></div>""")

da = 'https://www.youtube.com/watch?v=v9C9yckcWjQ&ab_channel=ArshGoyal'
st.video(da)

v = 'https://www.youtube.com/embed/nFQ22Wb6Qe8'
st.video(v)

s = 'https://www.youtube.com/watch?v=1QI0wDJeXO4&ab_channel=AnujBhaiya'
st.video(s)

dev = 'https://www.youtube.com/watch?v=qlHsAfrs3GE&ab_channel=GenieAshwani'
st.video(dev)

bc = 'https://www.youtube.com/watch?v=n_5oeZWbseY&ab_channel=AnujBhaiya'
st.video(bc)
