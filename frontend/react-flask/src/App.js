import './App.css';
import './components/hi.js'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
    <Routes>
      <Route path="/" element={<hi />}/>
    <div className="App">
      <p>My name is joe</p>
    </div>
    </Routes>
    </Router>
  );
}

export default App;
