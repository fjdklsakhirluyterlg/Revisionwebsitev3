import './App.css';
import './components/hi.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Route path="/" element={<hi />}/>
    <div className="App">
      <p>My name is joe</p>
    </div>
    </Router>
  );
}

export default App;
