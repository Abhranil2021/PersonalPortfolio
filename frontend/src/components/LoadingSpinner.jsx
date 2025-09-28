import React from 'react';
import { Loader2 } from 'lucide-react';

export const LoadingSpinner = ({ message = 'Loading...' }) => {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
      <div className="text-center">
        <Loader2 className="animate-spin w-12 h-12 mx-auto mb-4 text-blue-400" />
        <p className="text-gray-400 font-light">{message}</p>
      </div>
    </div>
  );
};

