import React, { useState, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom';
import ChatMessage from './ChatMessage';
import TypingIndicator from './TypingIndicator';

const AskAdvisorPage = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'advisor',
      content: "👋 **Welcome to your AI Investment Advisor!**\n\nI'm here to help you make informed investment decisions with:\n\n• **Real-time stock analysis** and recommendations\n• **Portfolio optimization** strategies\n• **Risk assessment** and market insights\n• **Sector analysis** and trend identification\n\nWhat investment question can I help you with today?",
      timestamp: new Date(),
      confidence: 1.0,
      sources: ["AI Investment Advisory System"]
    }
  ]);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);
  const textareaRef = useRef(null);
  const [showSuggestions, setShowSuggestions] = useState(true);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Auto-resize textarea
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = textareaRef.current.scrollHeight + 'px';
    }
  }, [currentQuestion]);

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
    setShowSuggestions(false);

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
        content: "⚠️ **Service Temporarily Unavailable**\n\nI apologize, but I'm having trouble processing your question right now. This could be due to:\n\n• **High server load** - Please try again in a moment\n• **Network connectivity** - Check your connection\n• **Maintenance** - Our systems may be updating\n\nPlease try asking about specific stocks, market trends, or investment strategies in a few minutes.",
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

  const suggestedQuestions = [
    {
      icon: '🎯',
      question: "Should I buy AAPL?",
      category: "Stock Analysis"
    },
    {
      icon: '🔮',
      question: "What's your outlook on the tech sector?",
      category: "Sector Insights"
    },
    {
      icon: '⚖️',
      question: "How should I diversify my portfolio?",
      category: "Portfolio Strategy"
    },
    {
      icon: '📈',
      question: "What are your top 3 stock picks?",
      category: "Recommendations"
    },
    {
      icon: '₿',
      question: "Is Bitcoin a good investment right now?",
      category: "Crypto Analysis"
    },
    {
      icon: '⚡',
      question: "What's the risk level of Tesla?",
      category: "Risk Assessment"
    },
    {
      icon: '🌍',
      question: "How's the market looking overall?",
      category: "Market Overview"
    },
    {
      icon: '🛡️',
      question: "What are the best low-risk investments?",
      category: "Conservative Options"
    }
  ];

  const handleSuggestedQuestion = (question) => {
    setCurrentQuestion(question);
    textareaRef.current?.focus();
    setShowSuggestions(false);
  };

  const clearChat = () => {
    setMessages([messages[0]]); // Keep only the welcome message
    setShowSuggestions(true);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container-fluid py-8">
        {/* Header */}
        <div className="mb-8 text-center">
          <div className="flex items-center justify-center mb-4">
            <div className="w-16 h-16 bg-gradient-to-r from-green-500 to-blue-600 rounded-2xl flex items-center justify-center mr-4">
              <span className="text-2xl">🤖</span>
            </div>
            <div className="text-left">
              <h1 className="heading-2 mb-0">AI Investment Advisor</h1>
              <p className="text-gray-400">Your Personal Financial Intelligence</p>
            </div>
          </div>
          <p className="text-lg text-secondary max-w-2xl mx-auto">
            Get personalized investment advice powered by comprehensive market analysis and real-time data
          </p>
        </div>

        <div className="max-w-6xl mx-auto">
          {/* Chat Container */}
          <div className="card p-0 mb-24" style={{ height: '55vh' }}>
            {/* Chat Header */}
            <div className="flex items-center justify-between p-6 border-b border-gray-700">
              <div className="flex items-center space-x-3">
                <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                <span className="text-green-400 font-medium">AI Advisor Online</span>
              </div>
              <button
                onClick={clearChat}
                className="btn btn-sm text-gray-400 hover:text-white hover:bg-gray-700"
              >
                🗑️ Clear Chat
              </button>
            </div>
            
            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto p-6 space-y-4" style={{ height: 'calc(55vh - 140px)' }}>
              {messages.map((message) => (
                <ChatMessage
                  key={message.id}
                  message={message.content}
                  isUser={message.type === 'user'}
                  timestamp={message.timestamp}
                  confidence={message.confidence}
                  sources={message.sources}
                  relevant_symbols={message.relevant_symbols}
                />
              ))}
              
              {isLoading && <TypingIndicator />}
              <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="border-t border-gray-700 p-6">
              <form onSubmit={handleSubmit} className="space-y-4">
                <div className="flex space-x-4">
                  <div className="flex-1">
                    <textarea
                      ref={textareaRef}
                      value={currentQuestion}
                      onChange={(e) => setCurrentQuestion(e.target.value)}
                      onKeyPress={handleKeyPress}
                      placeholder="Ask about investments, stocks, market trends, portfolio advice..."
                      className="w-full px-4 py-3 bg-gray-800 border border-gray-600 rounded-xl text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none min-h-[50px] max-h-32"
                      rows="1"
                      disabled={isLoading}
                    />
                  </div>
                  <button
                    type="submit"
                    disabled={!currentQuestion.trim() || isLoading}
                    className="btn btn-primary px-6 py-3 h-fit disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {isLoading ? (
                      <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                    ) : (
                      '🚀 Ask'
                    )}
                  </button>
                </div>
                
                <div className="flex items-center justify-between text-xs text-gray-500">
                  <span>Press Enter to send, Shift+Enter for new line</span>
                  <span>{currentQuestion.length}/500</span>
                </div>
              </form>
            </div>
          </div>

          {/* Suggested Questions - Now with maximum space below the chat */}
          {showSuggestions && messages.length <= 1 && (
            <div className="animate-fade-in-up mt-24">
              <h3 className="text-xl font-semibold mb-10 text-center">💡 Popular Questions</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16">
                {suggestedQuestions.map((item, index) => (
                  <button
                    key={index}
                    onClick={() => handleSuggestedQuestion(item.question)}
                    className="card p-4 text-left hover:border-blue-500 transition-all duration-200 group"
                  >
                    <div className="flex items-start space-x-3">
                      <span className="text-2xl group-hover:scale-110 transition-transform">{item.icon}</span>
                      <div className="flex-1">
                        <div className="text-sm text-blue-400 font-medium mb-1">{item.category}</div>
                        <div className="text-white group-hover:text-blue-300 transition-colors">
                          "{item.question}"
                        </div>
                      </div>
                      <span className="text-gray-500 group-hover:text-blue-400 transition-colors">→</span>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Quick Links */}
          <div className="flex flex-wrap justify-center gap-4 text-center mt-16">
            <Link
              to="/investments"
              className="btn btn-outline flex items-center space-x-2"
            >
              <span>📊</span>
              <span>View All Recommendations</span>
            </Link>
            <Link
              to="/news"
              className="btn btn-outline flex items-center space-x-2"
            >
              <span>📰</span>
              <span>Read Market News</span>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AskAdvisorPage;