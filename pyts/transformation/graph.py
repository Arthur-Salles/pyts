"""Code for Bag-of-patterns representation for time series."""

# Author: Arthur Salles <a.rezendesalles@gmail.com>
# License: BSD-3-Clause

from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils.validation import check_array, check_is_fitted
from ..bag_of_words import BagOfWords
from ..base import UnivariateTransformerMixin


class TstoGraph(BaseEstimator, UnivariateTransformerMixin):

    def __init__(self) -> None:
        super().__init__()
    
        print('Class Initialized')

    def fit(self, X=None, y=None):
        """Does nothing.

        Parameters
        ----------
        X : array-like, shape = (n_samples, n_timestamps)
            Input data

        y
            Ignored

        Returns
        -------
        self : object

        """

        return self