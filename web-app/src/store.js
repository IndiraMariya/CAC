import { writable } from 'svelte/store';
import { browser } from '$app/environment';

let stored = browser ? localStorage.readingData : '';

// Set the stored value or a sane default.
export const readingData = writable((browser && stored && JSON.parse(stored)) || []);

// Anytime the store changes, update the local storage value.
readingData.subscribe((value) => {
	if (browser) {
		return (localStorage.readingData = JSON.stringify(value));
	}
});
// or localStorage.setItem('content', value)
