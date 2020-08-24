import React, { useState, useEffect } from "react";
import { render } from "react-dom";

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: 20,
  },
  entryContainer: {
    display: 'flex',
    flexDirection: 'row',
    justifyContent: 'center',
  },
  innerContainer: {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start',
    padding: 10,
  },
  infoText: {
    fontFamily: 'sans-serif',
    fontSize: 20,
    margin: 50,
  },
  text: {
    fontFamily: 'sans-serif',
    fontSize: 18,
    padding: 15,
    margin: 0,
  },
  adjText: {
    fontFamily: 'sans-serif',
    fontSize: 18,
    padding: 5,
    paddingLeft: 15,
    paddingTop: 15,
    margin: 0,
  }
}

function App() {
  const [diary, setDiary] = useState({
    date: '',
    caption: '',
    rating: 0,
    adjectives: []
  })
  const [checkedIn, setCheckedIn] = useState(true)

  async function fetchDiary() {
    try {
      let response = await fetch('today/')
      if (response.status > 400) {
        setCheckedIn(false)
        response = await fetch('lastavailable/')
      }
      const json = await response.json()
      setDiary({...json[0]})
    } catch(err) {
      console.log(err)
    }
  }

  useEffect(() => { fetchDiary() }, [])

  return (
  <div style={styles.container}>
    {checkedIn ? (<p style={styles.infoText}>Thank you for checking in with me!</p>)
               : (<p style={styles.infoText}>I have not checked in today. Please check back later!</p>)}
    <div style={styles.entryContainer}>
      <div style={styles.innerContainer}>
        {checkedIn ? (<p style={styles.text}>What is the date today? </p>)
                   : (<p style={styles.text}>The most recent entry is for: </p>)}
        {checkedIn ? (<p style={styles.text}>How is my day going? </p>)
                   : (<p style={styles.text}>Caption of the day: </p>)}
        {checkedIn ? (<p style={styles.text}>If I were to rate my day: </p>)
                   : (<p style={styles.text}>Rating of the day: </p>)}
        {checkedIn ? (<p style={styles.text}>How am I feeling? </p>)
                   : (<p style={styles.text}>Adjectives of the day:</p>)}
      </div>
      <div style={styles.innerContainer}>
        <p style={styles.text}>{diary.date}</p>
        <p style={styles.text}>{diary.caption}</p>
        <p style={styles.text}>{diary.rating}/10</p>
        {/* <div style={{height: 30, backgroundColor: 'yellow'}}/> */}
        {diary.adjectives.map(adj => <p key={adj} style={styles.adjText}>{adj}</p>)}
      </div>
    </div>
  </div>
  );
}

export default App;


const container = document.getElementById("app");
render(<App />, container);