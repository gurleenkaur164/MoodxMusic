import React, {useState} from 'react';
import {getMood} from './api';

function App(){
    const [text, setText]= useState('');
    const [mood, setMood]= useState('');
    const [songs, setSongs]= useState([]);

    const hadnleSubmit= async(e)=>{
        e.preventDefault();
        const res= await getMood(text);
        setMood(res.data.mood);
        setSongs(res.data.songs);
    };

    return(
        <div style={{padding: '2rem'}}>
            <h1> Music Mood Recommendor</h1>
            <form onSubmit={handleSubmit}>
                <input 
                type="text"
                placeholder="Enter mood description"
                value={text}
                onChange={(e)=> setText(e.target.value)}
                required
                />
                <button type="submit">Find your songs</button>
            </form>
            {mood && (
        <>
          <h3>Predicted Mood: {mood}</h3>
          <ul>
            {songs.map((song, idx) => (
              <li key={idx}>{song}</li>
            ))}
          </ul>
        </>
      )}
        </div>
    );
}
export default App;