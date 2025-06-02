import React from 'react';
import { Link } from 'react-router-dom';

const ChatMessage = ({ message, isUser, timestamp, confidence, sources, relevant_symbols }) => {
  const formatTimestamp = (ts) => {
    return ts.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const formatMessageContent = (content) => {
    // Split content by lines and format for better readability
    const lines = content.split('\n');
    return lines.map((line, index) => {
      // Handle bold text (**text**)
      if (line.includes('**')) {
        const parts = line.split('**');
        return (
          <p key={index} className="mb-2">
            {parts.map((part, partIndex) => 
              partIndex % 2 === 1 ? 
                <strong key={partIndex} className="text-white font-semibold">{part}</strong> : 
                part
            )}
          </p>
        );
      }
      
      // Handle bullet points
      if (line.trim().startsWith('•') || line.trim().startsWith('-')) {
        return (
          <div key={index} className="flex items-start space-x-2 mb-1">
            <span className="text-blue-400 mt-1">•</span>
            <span>{line.replace(/^[•-]\s*/, '')}</span>
          </div>
        );
      }
      
      // Regular paragraphs
      if (line.trim()) {
        return <p key={index} className="mb-2">{line}</p>;
      }
      
      return <br key={index} />;
    });
  };

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-6 group`}>
      <div className={`max-w-4xl ${isUser ? 'order-2' : 'order-1'} w-full`}>
        {/* Message Header */}
        <div className={`flex items-center mb-3 ${isUser ? 'justify-end' : 'justify-start'}`}>
          <div className={`flex items-center space-x-3 ${isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
            <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold shadow-lg ${
              isUser 
                ? 'bg-gradient-to-r from-blue-500 to-blue-600 text-white' 
                : 'bg-gradient-to-r from-green-500 to-green-600 text-white'
            }`}>
              {isUser ? '👤' : '🤖'}
            </div>
            <div className={`${isUser ? 'text-right' : 'text-left'}`}>
              <div className="text-white font-medium text-sm">
                {isUser ? 'You' : 'AI Investment Advisor'}
              </div>
              <div className="text-gray-400 text-xs">
                {formatTimestamp(timestamp)}
              </div>
            </div>
          </div>
        </div>
        
        {/* Message Content */}
        <div className={`relative ${isUser ? 'ml-8' : 'mr-8'}`}>
          <div className={`card p-6 ${
            isUser 
              ? 'bg-gradient-to-r from-blue-600 to-blue-700 text-white border-blue-500' 
              : 'bg-gray-800 text-gray-100 border-gray-600'
          } transition-all duration-200 group-hover:shadow-xl`}>
            
            {/* Message Arrow */}
            <div className={`absolute top-4 ${
              isUser 
                ? '-right-2 border-l-blue-600' 
                : '-left-2 border-r-gray-800'
            } w-0 h-0 border-t-8 border-b-8 border-t-transparent border-b-transparent ${
              isUser ? 'border-l-8' : 'border-r-8'
            }`}></div>
            
            <div className="space-y-2">
              {formatMessageContent(message)}
            </div>
            
            {/* AI Message Metadata */}
            {!isUser && (confidence || sources || relevant_symbols) && (
              <div className="mt-6 pt-4 border-t border-gray-700">
                <div className="flex flex-wrap items-center justify-between gap-4 text-xs">
                  <div className="flex items-center space-x-6">
                    {confidence && (
                      <div className="flex items-center space-x-2">
                        <span className="text-gray-400">Confidence:</span>
                        <div className="flex items-center space-x-1">
                          <div className="w-16 h-2 bg-gray-700 rounded-full overflow-hidden">
                            <div 
                              className={`h-full rounded-full transition-all duration-500 ${
                                confidence >= 0.8 ? 'bg-green-500' : 
                                confidence >= 0.6 ? 'bg-yellow-500' : 'bg-red-500'
                              }`}
                              style={{ width: `${confidence * 100}%` }}
                            ></div>
                          </div>
                          <span className={`font-medium ${
                            confidence >= 0.8 ? 'text-green-400' : 
                            confidence >= 0.6 ? 'text-yellow-400' : 'text-red-400'
                          }`}>
                            {(confidence * 100).toFixed(0)}%
                          </span>
                        </div>
                      </div>
                    )}
                    
                    {relevant_symbols && relevant_symbols.length > 0 && (
                      <div className="flex items-center space-x-2">
                        <span className="text-gray-400">Related:</span>
                        <div className="flex flex-wrap gap-1">
                          {relevant_symbols.map((symbol, index) => (
                            <span 
                              key={index}
                              className="px-2 py-1 bg-blue-600/20 text-blue-400 rounded text-xs font-medium"
                            >
                              {symbol}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                  
                  {sources && sources.length > 0 && (
                    <div className="text-gray-500 text-right">
                      <span className="text-xs">Sources: {sources.join(', ')}</span>
                    </div>
                  )}
                </div>
                
                {/* Quick Action Buttons */}
                {relevant_symbols && relevant_symbols.length > 0 && (
                  <div className="mt-4 flex flex-wrap gap-2">
                    {relevant_symbols.map((symbol, index) => (
                      <Link
                        key={index}
                        to={`/investments?symbol=${symbol}`}
                        className="inline-flex items-center px-3 py-1.5 bg-gray-700 hover:bg-gray-600 rounded-lg text-xs text-blue-400 hover:text-blue-300 transition-colors duration-200 group"
                      >
                        <span className="mr-1">📊</span>
                        View {symbol} Details
                        <span className="ml-1 group-hover:translate-x-0.5 transition-transform">→</span>
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatMessage;