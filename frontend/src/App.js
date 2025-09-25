import React from 'react';
import Portfolio from './components/Portfolio';
import ErrorBoundary from './components/ErrorBoundary';
import './styles/index.css';

function App() {
  return (
    <ErrorBoundary>
      <div className="App">
        <Portfolio />
      </div>
    </ErrorBoundary>
  );
}

export default App;