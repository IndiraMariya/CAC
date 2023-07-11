import { createClient } from '@supabase/supabase-js'

export const supabase = createClient('https://rehftaccvqxocrqyrfam.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJlaGZ0YWNjdnF4b2NycXlyZmFtIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODkwMzE2MjAsImV4cCI6MjAwNDYwNzYyMH0.-dH8LXuy2nWKq8cnTM91pYsJoIQlDgCKXYsHd-yx-jU')