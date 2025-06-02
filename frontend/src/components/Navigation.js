import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navigation = () => {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  const navItems = [
    { path: '/', label: 'Home', icon: '🏠' },
    { path: '/news', label: 'News', icon: '📰' },
    { path: '/investments', label: 'Investments', icon: '📊' },
    { path: '/ask-advisor', label: 'AI Advisor', icon: '🤖' }
  ];

  return (
    <nav className="bg-gray-900/95 backdrop-blur-sm border-b border-gray-700 sticky top-0 z-50">
      <div className="container-fluid">
        <div className="flex justify-between h-16">
          {/* Logo Section */}
          <div className="flex items-center">
            <Link to="/" className="flex items-center space-x-3 group">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-200">
                <span className="text-white font-bold text-lg">H</span>
              </div>
              <div className="flex flex-col">
                <span className="text-white font-bold text-lg leading-tight">Hub Editor</span>
                <span className="text-xs text-gray-400 leading-tight">Investment Platform</span>
              </div>
            </Link>
          </div>
          
          {/* Navigation Items */}
          <div className="flex items-center space-x-2">
            {navItems.map((item) => {
              const isCurrentlyActive = isActive(item.path) || 
                (item.path !== '/' && location.pathname.startsWith(item.path + '/'));
              
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`
                    flex items-center space-x-2 px-4 py-2 rounded-lg text-sm font-medium 
                    transition-all duration-200 hover:scale-105
                    ${isCurrentlyActive 
                      ? 'text-white bg-gray-800 shadow-lg' 
                      : 'text-gray-300 hover:text-white hover:bg-gray-700'
                    }
                  `}
                >
                  <span className="text-base">{item.icon}</span>
                  <span className="hidden sm:block">{item.label}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;