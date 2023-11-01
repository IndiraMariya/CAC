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

function groupScoopsWithImages(scoops) {
	let newArticles = [];
	let lastNoPhoto = null;
	for (let i = 0; i < scoops.length; i++) {
		let firstArticle = scoops[i].article;
		if (firstArticle.articleData) {
			if (firstArticle.articleData.src) {
				newArticles.push(scoops[i]);
			} else {
				if (lastNoPhoto) {
					newArticles.push(lastNoPhoto);
					newArticles.push(scoops[i]);

					lastNoPhoto = null;
				} else {
					lastNoPhoto = scoops[i];
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

	// sort by date
	if (filterData[0].ascending != null) {
		sortedArticles.sort((a, b) => {
			return (
				(new Date(a.articleData['date']).getTime() - new Date(b.articleData['date']).getTime()) *
				(filterData[0].ascending ? 1 : -1)
			);
		});
	} else if (filterData[2].ascending != null) {
		sortedArticles.sort((a, b) => {
			return (
				(biasToNumber[a['bias']] - biasToNumber[b['bias']]) * (filterData[2].ascending ? 1 : -1)
			);
		});
	}

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
			for (let j = 0; j < Math.min(3, topics[i].tags.length); j++) {
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

export function sortData(topics, filterData) {
	// sort by popularity
	if (filterData[1].ascending != null) {
		topics.sort((a, b) => {
			return (a.articles.length - b.articles.length) * (filterData[1].ascending ? 1 : -1);
		});
	}

	return topics;
}

export function getData(topics, searchQuery, filterData) {
	let filteredTopics = filterDataBySearch(topics, searchQuery);
	let sortedTopics = sortData(filteredTopics, filterData);

	return sortedTopics;
}

// gets one article chosen from random from each topic and returns the "scoop" (article + relevant topic linkage)
export function getDailyScoops(topics) {
	let today = new Date().setHours(0, 0, 0, 0); // TODO: remove the yesterday article

	let scoops = [];

	for (let i = 0; i < topics.length; i++) {
		let dailyArticles = topics[i].articles.filter(
			(article) => new Date(article.articleData.date).setHours(0, 0, 0, 0) == today
		);

		// there are articles from today
		if (dailyArticles.length > 0) {
			scoops.push({
				numArticles: dailyArticles.length,
				topic: topics[i].topic,
				keywords: topics[i].tags,
				article: dailyArticles[Math.floor(Math.random() * dailyArticles.length)] // random article to represent the "scoop"
			});
		}
	}
	scoops.sort((a, b) => {
		return b.numArticles - a.numArticles;
	});

	return groupScoopsWithImages(scoops);
}

export function getPropertyData(readingData, property, label, colorFunc) {
	let props = {};

	for (let i = 0; i < readingData.length; i++) {
		let prop = readingData[i][property];
		if (prop in props) {
			props[prop] += 1;
		} else {
			props[prop] = 1;
		}
	}

	let propsList = [];
	for (let prop in props) {
		propsList.push([prop, props[prop] / readingData.length]);
	}
	propsList.sort((a, b) => b[1] - a[1]);

	let labels = [];
	let values = [];
	let colors = [];
	for (let i = 0; i < propsList.length; i++) {
		labels.push(propsList[i][0]);
		values.push(propsList[i][1]);
		if (colorFunc) {
			colors.push(colorFunc(propsList[i][0]));
		} else {
			colors.push('rgba(0, 0, 0, 0.1)');
		}
	}

	const data = {
		labels: labels,
		datasets: [
			{
				data: values,
				backgroundColor: colors,
				borderWidth: 0
			}
		]
	};

	return data;
}

export const leanToColor = {
	'Far Left': 'rgba(59,73,155,0.5)',
	Left: 'rgba(59,73,155,0.25)',
	'Far Right': 'rgba(229, 49, 49, 0.5)',
	Right: 'rgba(229, 49, 49, 0.25)'
};

// source leans
let sourceToLean = {
	'New York Times': 'Far Left',
	'Fox News': 'Right',
	'Washington Post': 'Left'
};

export function getLean(source) {
	return sourceToLean[source];
}

export function getLeanColor(lean) {
	return leanToColor[lean];
}

export function getSourceColor(source) {
	return leanToColor[getLean(source)];
}
