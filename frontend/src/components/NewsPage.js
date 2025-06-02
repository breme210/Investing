import React, { useState, useEffect } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import NewsCard from './NewsCard';

const NewsPage = () => {
  const [articles, setArticles] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchParams, setSearchParams] = useSearchParams();

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    fetchCategories();
    // Get category from URL params
    const categoryFromUrl = searchParams.get('category');
    if (categoryFromUrl) {
      setSelectedCategory(categoryFromUrl);
    }
  }, []);

  useEffect(() => {
    fetchArticles();
  }, [selectedCategory]);

  const fetchCategories = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/news/categories/list`);
      if (!response.ok) throw new Error('Failed to fetch categories');
      const data = await response.json();
      setCategories(data);
    } catch (err) {
      console.error('Error fetching categories:', err);
    }
  };

  const fetchArticles = async () => {
    try {
      setLoading(true);
      const url = selectedCategory 
        ? `${backendUrl}/api/news?category=${encodeURIComponent(selectedCategory)}`
        : `${backendUrl}/api/news`;
      
      const response = await fetch(url);
      if (!response.ok) throw new Error('Failed to fetch articles');
      
      const data = await response.json();
      setArticles(data);
      setError(null);
    } catch (err) {
      setError('Failed to load articles. Please try again later.');
      console.error('Error fetching articles:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    // Update URL params
    if (category) {
      setSearchParams({ category });
    } else {
      setSearchParams({});
    }
  };

  const getCategoryConfig = (category) => {
    const configs = {
      'Technology': { icon: '💻', color: 'blue' },
      'Product Updates': { icon: '🚀', color: 'green' },
      'Industry News': { icon: '🏢', color: 'purple' },
      'Company News': { icon: '📢', color: 'orange' },
      'Market Analysis': { icon: '📊', color: 'red' },
      'Financial': { icon: '💰', color: 'yellow' }
    };
    return configs[category] || { icon: '📰', color: 'gray' };
  };

  const EmptyStateComponent = () => (
    <div className="text-center py-20">
      <div className="w-24 h-24 mx-auto mb-8 bg-gray-800 rounded-full flex items-center justify-center">
        <span className="text-4xl">📰</span>
      </div>
      <h3 className="heading-3 mb-4">No News Available</h3>
      <p className="text-gray-400 mb-8 max-w-md mx-auto">
        We're currently working on bringing you the latest financial news and market updates.
      </p>
      <div className="space-y-4">
        <button
          onClick={fetchArticles}
          className="btn btn-primary mr-4"
        >
          🔄 Refresh News
        </button>
        <p className="text-sm text-gray-500">
          Check out our <a href="/ask-advisor" className="text-blue-400 hover:text-blue-300">AI Investment Advisor</a> for real-time market insights
        </p>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container-fluid py-8">
        {/* Header */}
        <div className="mb-12 text-center">
          <h1 className="heading-1 mb-6">Financial News & Insights</h1>
          <p className="text-xl text-secondary max-w-3xl mx-auto">
            Stay ahead of the markets with curated financial news, analysis, and expert insights. 
            Get the information you need to make informed investment decisions.
          </p>
        </div>

        {/* Featured Section */}
        <div className="mb-12 p-8 bg-gradient-to-r from-blue-600/10 to-purple-600/10 rounded-2xl border border-blue-500/20">
          <div className="text-center">
            <h2 className="text-2xl font-semibold mb-4 flex items-center justify-center">
              <span className="mr-3">⚡</span>
              Breaking: Real-Time Market Updates
            </h2>
            <p className="text-gray-300 mb-6">
              Our AI continuously monitors market movements and breaking news to keep you informed
            </p>
            <a href="/ask-advisor" className="btn btn-gradient">
              🤖 Get Live Market Analysis
            </a>
          </div>
        </div>

        {/* Category Filter */}
        {categories.length > 0 && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-6 flex items-center">
              <span className="mr-2">🎯</span>
              Browse by Category
            </h3>
            <div className="flex flex-wrap gap-3">
              <button
                onClick={() => handleCategoryChange('')}
                className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${
                  selectedCategory === ''
                    ? 'bg-blue-600 text-white shadow-lg'
                    : 'bg-gray-800 text-gray-300 hover:bg-gray-700 hover:text-white'
                }`}
              >
                <span>📰</span>
                <span>All News</span>
                <span className="bg-white/20 px-2 py-1 rounded-full text-xs">
                  {categories.reduce((sum, cat) => sum + cat.count, 0)}
                </span>
              </button>
              
              {categories.map((category) => {
                const config = getCategoryConfig(category.category);
                return (
                  <button
                    key={category.category}
                    onClick={() => handleCategoryChange(category.category)}
                    className={`flex items-center space-x-2 px-4 py-3 rounded-xl text-sm font-medium transition-all duration-200 ${
                      selectedCategory === category.category
                        ? 'bg-blue-600 text-white shadow-lg'
                        : 'bg-gray-800 text-gray-300 hover:bg-gray-700 hover:text-white'
                    }`}
                  >
                    <span>{config.icon}</span>
                    <span>{category.category}</span>
                    <span className="bg-white/20 px-2 py-1 rounded-full text-xs">
                      {category.count}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Content */}
        {loading ? (
          <div className="flex justify-center items-center py-20">
            <div className="text-center">
              <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
              <p className="text-gray-400">Loading latest news...</p>
            </div>
          </div>
        ) : error ? (
          <div className="text-center py-16">
            <div className="w-16 h-16 mx-auto mb-6 bg-red-600/20 rounded-full flex items-center justify-center">
              <span className="text-2xl">⚠️</span>
            </div>
            <h3 className="text-xl font-semibold text-red-400 mb-4">Error Loading News</h3>
            <div className="text-gray-400 mb-6">{error}</div>
            <button
              onClick={fetchArticles}
              className="btn btn-primary"
            >
              🔄 Try Again
            </button>
          </div>
        ) : articles.length === 0 ? (
          <EmptyStateComponent />
        ) : (
          <>
            {/* Results Header */}
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-2xl font-semibold text-white">
                  {selectedCategory || 'Latest News'}
                </h2>
                <p className="text-gray-400">
                  {articles.length} article{articles.length !== 1 ? 's' : ''} found
                </p>
              </div>
              
              {selectedCategory && (
                <button
                  onClick={() => handleCategoryChange('')}
                  className="btn btn-outline text-sm"
                >
                  ← View All News
                </button>
              )}
            </div>

            {/* News Articles Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
              {articles.map((article, index) => (
                <div 
                  key={article.id}
                  className="animate-fade-in-up"
                  style={{ animationDelay: `${index * 0.1}s` }}
                >
                  <NewsCard article={article} />
                </div>
              ))}
            </div>

            {/* Newsletter Signup */}
            <div className="text-center mt-16 py-12 bg-gradient-to-r from-green-600/10 to-blue-600/10 rounded-2xl">
              <h3 className="text-2xl font-semibold mb-4">Stay Informed with Daily Updates</h3>
              <p className="text-gray-400 mb-6 max-w-2xl mx-auto">
                Get the latest financial news and market analysis delivered to your inbox.
              </p>
              <a href="/ask-advisor" className="btn btn-gradient btn-lg">
                📧 Subscribe to Newsletter
              </a>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default NewsPage;