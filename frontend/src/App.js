import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import HomePage from './components/HomePage';
import NewsPage from './components/NewsPage';
import NewsDetail from './components/NewsDetail';
import InvestmentsPage from './components/InvestmentsPage';
import InvestmentDetail from './components/InvestmentDetail';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <main className="min-h-screen">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/news" element={<NewsPage />} />
            <Route path="/news/:id" element={<NewsDetail />} />
            <Route path="/investments" element={<InvestmentsPage />} />
            <Route path="/investments/:id" element={<InvestmentDetail />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;