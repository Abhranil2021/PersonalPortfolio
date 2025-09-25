import React from 'react';
import { AlertTriangle, RefreshCw } from 'lucide-react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    });

    // Log error to console in development
    if (process.env.NODE_ENV === 'development') {
      console.error('ErrorBoundary caught an error:', error, errorInfo);
    }
  }

  handleRetry = () => {
    this.setState({ hasError: false, error: null, errorInfo: null });
    window.location.reload();
  };

  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
          <div className="max-w-md mx-auto text-center px-4">
            <div className="bg-red-900/20 border border-red-500/30 rounded-lg p-8">
              <AlertTriangle size={48} className="text-red-400 mx-auto mb-4" />
              <h2 className="text-xl font-light mb-4 text-red-400">
                Something went wrong
              </h2>
              <p className="text-gray-300 mb-6 text-sm">
                The application encountered an unexpected error. This has been logged for review.
              </p>
              
              {process.env.NODE_ENV === 'development' && this.state.error && (
                <details className="text-left mb-4 bg-gray-800 p-4 rounded text-xs">
                  <summary className="cursor-pointer text-yellow-400 mb-2">
                    Error Details (Development)
                  </summary>
                  <pre className="text-red-300 whitespace-pre-wrap">
                    {this.state.error.toString()}
                    {this.state.errorInfo.componentStack}
                  </pre>
                </details>
              )}
              
              <button
                onClick={this.handleRetry}
                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 text-sm font-light transition-colors flex items-center space-x-2 mx-auto"
              >
                <RefreshCw size={16} />
                <span>Reload Application</span>
              </button>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;