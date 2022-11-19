# UI with python
* Create virtual Envornment
    * `python -m ven <name>`
        * `.\<named>\Scripts\activate`
    * install all packages from **requirements.txt**
        * `pip install -r requirements.txt`    
    * Create file **app.py**
        * #### Example1: 
```
import streamlit as st
st.write("NED Machine Learning AI Application")
``` 
Run your application now:
```
streamlit run app.py
```

#### Example2: 
```
import streamlit as st

x = st.slider("X")
st.write(x,"NED Machine Learning AI Application Pakistan zinda bad", x*x)
```

### Example3:
```
import streamlit as st
import pandas as pd

data_cache = st.cache(pd.read_csv)

data = data_cache("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

species_label = st.selectbox("Select specie:",data.species.unique())

st.write(data[data.species==species_label])
```

### streamlit
### kivy
### django
### flask