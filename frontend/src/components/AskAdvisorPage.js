import React, { useState, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom';

const AskAdvisorPage = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'advisor',
      content: "Hello! I'm your AI Investment Advisor. I can help you with investment questions about stocks, indices, commodities, portfolio strategies, and market analysis. What would you like to know?",
      timestamp: new Date(),
      confidence: 1.0,
      sources: ["AI Investment Advisory System"]
    }
  ]);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!currentQuestion.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      type: 'user',
      content: currentQuestion.trim(),
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setCurrentQuestion('');
    setIsLoading(true);

    try {
      const response = await fetch(`${backendUrl}/api/investments/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: userMessage.content,
          user_id: 'frontend_user'
        })
      });

      if (!response.ok) {
        throw new Error('Failed to get response from advisor');
      }

      const data = await response.json();

      const advisorMessage = {
        id: Date.now() + 1,
        type: 'advisor',
        content: data.answer,
        timestamp: new Date(),
        confidence: data.confidence,
        sources: data.sources,
        relevant_symbols: data.relevant_symbols
      };

      setMessages(prev => [...prev, advisorMessage]);
    } catch (error) {
      console.error('Error asking advisor:', error);
      const errorMessage = {
        id: Date.now() + 1,
        type: 'advisor',
        content: "I apologize, but I'm having trouble processing your question right now. Please try again in a moment, or ask about specific stocks, market trends, or investment strategies.",
        timestamp: new Date(),
        confidence: 0.5,
        sources: ["Error handling system"]
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const formatTimestamp = (timestamp) => {
    return timestamp.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const renderMessage = (message) => {
    const isUser = message.type === 'user';
    
    return (
      <div key={message.id} className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-6`}>
        <div className={`max-w-3xl ${isUser ? 'order-2' : 'order-1'}`}>
          {/* Message header */}
          <div className={`flex items-center mb-2 ${isUser ? 'justify-end' : 'justify-start'}`}>
            <div className={`flex items-center space-x-2 ${isUser ? 'flex-row-reverse space-x-reverse' : ''}`}>
              <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold ${
                isUser ? 'bg-blue-600 text-white' : 'bg-green-600 text-white'
              }`}>
                {isUser ? 'U' : 'AI'}
              </div>
              <span className="text-gray-400 text-sm">
                {isUser ? 'You' : 'AI Advisor'} • {formatTimestamp(message.timestamp)}
              </span>
            </div>
          </div>
          
          {/* Message content */}
          <div className={`px-4 py-3 rounded-lg ${
            isUser 
              ? 'bg-blue-600 text-white' 
              : 'bg-gray-800 text-gray-100 border border-gray-700'
          }`}>
            <div className="whitespace-pre-wrap">{message.content}</div>
            
            {/* Advisor message metadata */}
            {!isUser && (
              <div className="mt-3 pt-3 border-t border-gray-700">
                <div className="flex flex-wrap items-center justify-between text-xs text-gray-400">
                  <div className="flex items-center space-x-4">
                    {message.confidence && (
                      <span className="flex items-center space-x-1">
                        <span>Confidence:</span>
                        <span className={`font-medium ${
                          message.confidence >= 0.8 ? 'text-green-400' : 
                          message.confidence >= 0.6 ? 'text-yellow-400' : 'text-red-400'
                        }`}>
                          {(message.confidence * 100).toFixed(0)}%
                        </span>
                      </span>
                    )}
                    {message.relevant_symbols && message.relevant_symbols.length > 0 && (
                      <span className="flex items-center space-x-1">
                        <span>Related:</span>
                        <span className="text-blue-400">
                          {message.relevant_symbols.join(', ')}
                        </span>
                      </span>
                    )}
                  </div>
                  {message.sources && message.sources.length > 0 && (
                    <span className="text-gray-500">
                      Sources: {message.sources.join(', ')}
                    </span>
                  )}
                </div>
                
                {/* Quick action buttons for symbols */}
                {message.relevant_symbols && message.relevant_symbols.length > 0 && (
                  <div className="mt-2 flex flex-wrap gap-2">
                    {message.relevant_symbols.map((symbol, index) => (
                      <Link
                        key={index}
                        to={`/investments?asset_type=stock`}
                        className="inline-flex items-center px-2 py-1 bg-gray-700 hover:bg-gray-600 rounded text-xs text-blue-400 hover:text-blue-300 transition-colors duration-200"
                      >
                        View {symbol} Details →
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    );
  };

  const suggestedQuestions = [
    "Should I buy AAPL?",
    "What's your outlook on the tech sector?",
    "How should I diversify my portfolio?",
    "What are your top 3 stock picks?",
    "Is Bitcoin a good investment right now?",
    "What's the risk level of Tesla?",
    "How's the market looking overall?",
    "What are the best low-risk investments?"
  ];

  const handleSuggestedQuestion = (question) => {
    setCurrentQuestion(question);
    textareaRef.current?.focus();
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8 text-center">
          <h1 className="text-4xl font-bold mb-4">
            AI Investment Advisor
          </h1>
          <p className="text-gray-400 text-lg">
            Get personalized investment advice powered by comprehensive market analysis
          </p>
        </div>

        {/* Chat container */}
        <div className="bg-gray-800 rounded-lg border border-gray-700 flex flex-col" style={{ height: '70vh' }}>
          {/* Messages area */}
          <div className="flex-1 overflow-y-auto p-6">
            {messages.map(renderMessage)}
            {isLoading && (
              <div className="flex justify-start mb-6">
                <div className="max-w-3xl">
                  <div className="flex items-center mb-2">
                    <div className="w-8 h-8 rounded-full bg-green-600 text-white flex items-center justify-center text-sm font-bold mr-2">
                      AI
                    </div>
                    <span className="text-gray-400 text-sm">AI Advisor is thinking...</span>
                  </div>
                  <div className="bg-gray-700 rounded-lg px-4 py-3">
                    <div className="flex space-x-1">
                      <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                      <div className="w-2 h-2 bg-gray-500 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                    </div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input area */}
          <div className="border-t border-gray-700 p-4">
            <form onSubmit={handleSubmit} className="flex space-x-3">
              <div className="flex-1">
                <textarea
                  ref={textareaRef}
                  value={currentQuestion}
                  onChange={(e) => setCurrentQuestion(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder="Ask about investments, stocks, market trends, portfolio advice..."
                  className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
                  rows="3"
                  disabled={isLoading}
                />
              </div>
              <button
                type="submit"
                disabled={!currentQuestion.trim() || isLoading}
                className="px-6 py-3 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed text-white rounded-lg font-medium transition-colors duration-200 self-end"
              >
                {isLoading ? (
                  <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                ) : (
                  'Ask'
                )}
              </button>
            </form>
            
            <div className="mt-3 text-xs text-gray-500">
              Press Enter to send, Shift+Enter for new line
            </div>
          </div>
        </div>

        {/* Suggested questions */}
        {messages.length <= 1 && (
          <div className="mt-6">
            <h3 className="text-lg font-semibold mb-4">Try asking about:</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {suggestedQuestions.map((question, index) => (
                <button
                  key={index}
                  onClick={() => handleSuggestedQuestion(question)}
                  className="text-left p-3 bg-gray-800 hover:bg-gray-700 border border-gray-700 hover:border-gray-600 rounded-lg transition-colors duration-200 text-gray-300 hover:text-white"
                >
                  "{question}"
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Quick links */}
        <div className="mt-8 flex justify-center space-x-6">
          <Link
            to="/investments"
            className="text-blue-400 hover:text-blue-300 transition-colors duration-200"
          >
            View All Recommendations →
          </Link>
          <Link
            to="/news"
            className="text-blue-400 hover:text-blue-300 transition-colors duration-200"
          >
            Read Market News →
          </Link>
        </div>
      </div>
    </div>
  );
};

export default AskAdvisorPage;