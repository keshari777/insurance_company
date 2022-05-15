import "./App.css";
import PolicyComponent from "./views/PolicyComponent";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import PolicyPerMonth from "./views/Analytics";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<PolicyComponent />} />
          <Route path="/charts" element={<PolicyPerMonth />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
