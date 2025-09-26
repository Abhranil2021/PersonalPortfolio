import React from 'react';
import Portfolio from './components/Portfolio';
import ErrorBoundary from './components/ErrorBoundary';
import './styles/index.css';

import { SpeedInsights } from "@vercel/speed-insights/react";

function App() {
  return (
    <ErrorBoundary>
      <div className="App">
        <Portfolio />
        {/* Add Vercel Speed Insights here */}
        <SpeedInsights />
      </div>
    </ErrorBoundary>
  );
}

export default App;