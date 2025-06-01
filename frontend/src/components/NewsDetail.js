import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';

const NewsDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const backendUrl = process.env.REACT_APP_BACKEND_URL || import.meta.env.REACT_APP_BACKEND_URL;

  useEffect(() => {
    fetchArticle();
  }, [id]);

  const fetchArticle = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${backendUrl}/api/news/${id}`);
      
      if (!response.ok) {
        if (response.status === 404) {
          setError('Article not found');
        } else {
          throw new Error('Failed to fetch article');
        }
        return;
      }
      
      const data = await response.json();
      setArticle(data);
      setError(null);
    } catch (err) {
      setError('Failed to load article. Please try again later.');
      console.error('Error fetching article:', err);
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getCategoryColor = (category) => {
    const colors = {
      'Technology': 'bg-blue-600',
      'Product Updates': 'bg-green-600',
      'Industry News': 'bg-purple-600',
      'Company News': 'bg-orange-600'
    };
    return colors[category] || 'bg-gray-600';
  };

  const getImageForCategory = (category) => {
    const images = {
      'Technology': 'https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
      'Product Updates': 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
      'Industry News': 'https://images.unsplash.com/photo-1504711434969-e33886168f5c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
      'Company News': 'https://images.pexels.com/photos/7054384/pexels-photo-7054384.jpeg?auto=compress&cs=tinysrgb&w=1200'
    };
    return images[category] || images['Technology'];
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex justify-center items-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center py-12">
            <div className="text-red-400 mb-4 text-lg">{error}</div>
            <div className="space-x-4">
              <button
                onClick={fetchArticle}
                className="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md transition-colors duration-200"
              >
                Try Again
              </button>
              <Link
                to="/news"
                className="bg-gray-600 hover:bg-gray-700 px-4 py-2 rounded-md transition-colors duration-200 inline-block"
              >
                Back to News
              </Link>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!article) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Back Button */}
        <button
          onClick={() => navigate(-1)}
          className="flex items-center text-gray-400 hover:text-white mb-6 transition-colors duration-200"
        >
          <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          Back to News
        </button>

        {/* Article Header */}
        <header className="mb-8">
          <div className="flex items-center mb-4">
            <span className={`px-3 py-1 rounded-full text-sm font-medium text-white ${getCategoryColor(article.category)} mr-4`}>
              {article.category}
            </span>
            <span className="text-gray-400">{article.read_time} min read</span>
          </div>
          
          <h1 className="text-4xl md:text-5xl font-bold mb-4 leading-tight">
            {article.title}
          </h1>
          
          <p className="text-xl text-gray-400 mb-6 leading-relaxed">
            {article.summary}
          </p>
          
          <div className="flex items-center justify-between text-gray-500 mb-6">
            <span>By {article.author}</span>
            <span>{formatDate(article.publish_date)}</span>
          </div>
        </header>

        {/* Featured Image */}
        <div className="mb-8">
          <img
            src={article.image_url || getImageForCategory(article.category)}
            alt={article.title}
            className="w-full h-64 md:h-96 object-cover rounded-lg"
          />
        </div>

        {/* Article Content */}
        <article className="prose prose-lg prose-invert max-w-none mb-8">
          <div 
            className="text-gray-300 leading-relaxed"
            style={{ 
              fontSize: '1.125rem', 
              lineHeight: '1.75',
              whiteSpace: 'pre-line'
            }}
          >
            {article.content}
          </div>
        </article>

        {/* Tags */}
        {article.tags.length > 0 && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-3">Tags</h3>
            <div className="flex flex-wrap gap-2">
              {article.tags.map((tag, index) => (
                <span
                  key={index}
                  className="px-3 py-1 bg-gray-800 text-gray-300 rounded-full text-sm border border-gray-700"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
        )}

        {/* Navigation */}
        <div className="border-t border-gray-800 pt-8">
          <div className="flex justify-between items-center">
            <Link
              to="/news"
              className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-md transition-colors duration-200 font-medium"
            >
              View All Articles
            </Link>
            <Link
              to={`/news?category=${encodeURIComponent(article.category)}`}
              className="text-gray-400 hover:text-white transition-colors duration-200"
            >
              More in {article.category}
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NewsDetail;