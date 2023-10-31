let biasToNumber = {
	'mostly objective': 0,
	'slightly objective': 1,
	'slightly subjective': 2,
	'mostly subjective': 3
};

function shouldFilterByTag(searchText) {
	return searchText.trim().substring(0, 1) == '#';
}

function filterArticles(articles, searchText) {
	// TODO: implement fuzzy search???
	let matchingArticles = [];
	let nonMatchingArticles = [];
	for (let i = 0; i < articles.length; i++) {
		if (
			articles[i].articleData.title.toLowerCase().includes(searchText) ||
			articles[i].articleData.title.toLowerCase().includes(searchText)
		) {
			matchingArticles.push(articles[i]);
		} else {
			nonMatchingArticles.push(articles[i]);
		}
	}

	return {
		matchingArticles: matchingArticles,
		nonMatchingArticles: nonMatchingArticles
	};
}

function groupArticlesWithImages(articles) {
	let newArticles = [];
	let lastNoPhoto = null;
	for (let i = 0; i < articles.length; i++) {
		let firstArticle = articles[i];
		if (firstArticle.articleData) {
			if (firstArticle.articleData.src) {
				newArticles.push(firstArticle);
			} else {
				if (lastNoPhoto) {
					newArticles.push(lastNoPhoto);
					newArticles.push(firstArticle);

					lastNoPhoto = null;
				} else {
					lastNoPhoto = firstArticle;
				}
			}
		}
	}
	if (lastNoPhoto) {
		newArticles.push(lastNoPhoto);
	}
	return newArticles;
}

function sortArticles(articles, filterData) {
	let sortedArticles = articles.slice();
	sortedArticles.sort((a, b) => {
		return (
			// date
			(filterData[0].ascending != null &&
				(new Date(a.articleData[filterData[0].value]).getTime() -
					new Date(b.articleData[filterData[0].value]).getTime()) *
					(filterData[0].ascending ? 1 : -1)) ||
			// bias
			(filterData[2].ascending != null &&
				(biasToNumber[a.articleData[filterData[2].value]] -
					biasToNumber[b.articleData[filterData[2].value]]) *
					(filterData[2].ascending ? 1 : -1))
		);
	});
	return sortedArticles;
}

// takes in a list of articles -> returns a list of articles with articles that have no images (src values) grouped together
export function getArticles(articles, filterData, searchText) {
	let peekArticles = articles.slice();
	let hiddenArticles = [];

	// article search
	if (!shouldFilterByTag(searchText)) {
		let { matchingArticles, nonMatchingArticles } = filterArticles(articles, searchText);

		peekArticles = matchingArticles;
		hiddenArticles = nonMatchingArticles;
	}

	const res = {
		peek: groupArticlesWithImages(sortArticles(peekArticles, filterData)),
		hidden: groupArticlesWithImages(sortArticles(hiddenArticles, filterData))
	};

	return res;
}

export function filterDataBySearch(topics, searchQuery) {
	let newTopics = [];
	// search by tag
	if (shouldFilterByTag(searchQuery)) {
		let strippedQuery = searchQuery.trim().substring(1);

		for (let i = 0; i < topics.length; i++) {
			for (let j = 0; j < topics[i].tags.length; j++) {
				if (topics[i].tags[j].includes(strippedQuery)) {
					newTopics.push(topics[i]);
					break;
				}
			}
		}
	} else {
		// TODO: make this actually work
		newTopics = topics.slice();
	}

	return newTopics;
}
