import React from 'react';

const TypingIndicator = () => {
  return (
    <div className="flex justify-start mb-6">
      <div className="max-w-4xl w-full">
        {/* Header */}
        <div className="flex items-center mb-3">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-full bg-gradient-to-r from-green-500 to-green-600 flex items-center justify-center text-sm font-bold shadow-lg">
              🤖
            </div>
            <div>
              <div className="text-white font-medium text-sm">AI Investment Advisor</div>
              <div className="text-gray-400 text-xs">Analyzing your request...</div>
            </div>
          </div>
        </div>
        
        {/* Typing Animation */}
        <div className="mr-8">
          <div className="card bg-gray-800 border-gray-600 p-6">
            <div className="flex items-center space-x-2">
              <div className="flex space-x-1">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
              </div>
              <span className="text-gray-400 text-sm ml-3">Processing market data and generating insights...</span>
            </div>
            
            {/* Progress bar animation */}
            <div className="mt-4">
              <div className="w-full bg-gray-700 rounded-full h-1">
                <div className="bg-gradient-to-r from-blue-500 to-green-500 h-1 rounded-full animate-pulse" style={{ width: '60%' }}></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;