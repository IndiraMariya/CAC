  import { supabase } from "$lib/components/supabaseClient.js";

  export async function load() {
    const { data } = await supabase.from("topics").select();
    return {
      topics: data ?? [],
    };
  }