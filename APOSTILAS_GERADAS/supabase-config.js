// CONFIGURAÇÃO SUPABASE - NÃO COMMITAR ESTE ARQUIVO
// Credenciais do projeto: rovcqovxkyfrccerkuls
// Dashboard: https://supabase.com/dashboard/project/rovcqovxkyfrccerkuls

window.SUPABASE_URL = 'https://rovcqovxkyfrccerkuls.supabase.co';
window.SUPABASE_ANON_KEY = 'sb_publishable_uHYDqeToRM4sNpwTEAV1EA_iPGB7FUy';

// NOTA: A secret key NÃO deve ser usada no frontend (apenas server-side).
// A connection string (postgresql://...) é para uso com Supabase CLI / migrações locais.

// Tabela necessária no Supabase (execute no SQL Editor do Dashboard):
/*
CREATE TABLE anotacoes (
  topic_id TEXT PRIMARY KEY,
  conteudo TEXT,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Habilitar RLS (Row Level Security)
ALTER TABLE anotacoes ENABLE ROW LEVEL SECURITY;

-- Policy para permitir leitura/escrita com anon key
CREATE POLICY "Allow anon read/write" ON anotacoes
  FOR ALL USING (true) WITH CHECK (true);
*/