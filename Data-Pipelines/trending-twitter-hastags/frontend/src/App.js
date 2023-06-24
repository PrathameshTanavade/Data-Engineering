
import './App.css';
import  './fonts/fontawesome-all.min.css';

import React, {useState} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import HashtagsView from './components/hashtag_view';



function App() {


  const [trending_hashtags, setHashtag] = useState([{}])
  const [city,setCity]=useState(' ')

  const addGetHandler = () => {
     axios.get('http://localhost:8000/city/',{
      params: {
        'city': city 
      }
    })
      .then(res => {
        setHashtag(res.data)
      }) 
    
  };


  return (
    <div className='header'>  
    <div className="App header list-group-item justify-content-center align-items-center" style={{"min-height":'100vh'}} >
      <h1  style={{"paddingTop":"3em"}}styleName="max-width: 20rem;">Trending <span class="icon brands fa-twitter"></span>#Hashtag </h1>
      <h6 >By Prathamesh Tanavade</h6>
      <span> 
        <input className="align-items-center mx-auto mb-2 form-control titleIn" style={{width:'400px', 'marginTop':'5em'}} onChange={event => setCity(event.target.value)} placeholder='Enter City Name eg.Ohio'/> 
        <button className="button" style={{'borderRadius':'50px',"font-weight":"bold",'marginTop':'2em','marginBottom':'4em'}} onClick={addGetHandler} >Get Trends</button>
      </span>
      
      <div>
        < HashtagsView hashtagList={trending_hashtags} />
      </div>
     </div>
    </div> 



    
  );
}

export default App;
