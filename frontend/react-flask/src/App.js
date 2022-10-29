import logo from './logo.svg';
import './App.css';
import { useEffect } from 'react/cjs/react.production.min';
import { useState } from 'react';

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <p>{currentTime}</p>
      </header>
    </div>
  );
}

export default App;
