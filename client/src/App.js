import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import Header from './Header'
import Home from './Home'
import Footer from './Footer'
import Login from './Login'

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/">
            <Header />
            <Home />
            <Footer />
          </Route>
        </ Switch>
      </div>
  </ Router>
  );
}

export default App;
