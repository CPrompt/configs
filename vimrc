"------------------------------------
"	general settings
"------------------------------------
set nocompatible		"getout of vi-compatible mode
set history=1000
set undolevels=200
set cf				"enable error files and error jumping
filetype on
set ffs=unix,dos,mac		"support these filetypes in this order
set viminfo+=!
"setlocal spell spelllang=en_us	"turn on spellcheck
syntax on			"turn on syntax highlighting
set clipboard=unnamedplus	"set the clipboard so we can access it
" don't close if unsaved changes
set confirm
"-------------------------
" User interface settings
"-------------------------
set lsp=0		" space it out a little more (easier to read)
set wildmenu		" turn on wild menu
set ruler               " Show the line and column numbers of the cursor.
set cmdheight=2		" set command bar height
set showcmd             " Show (partial) command in status line.
set showmode            " Show current mode.
set ignorecase          " Case insensitive matching.
set scrolloff=5         " Keep a context when scrolling.
set modeline            " Enable modeline.
set title		" show title in console title bar
set esckeys             " Cursor keys in insert mode.
set gdefault            " Use 'g' flag by default with :s/foo/bar/.
set magic               " Use 'magic' patterns (extended regular expressions).
set ttyscroll=0         " Turn off scrolling (this is faster).
set ttyfast             " We have a fast terminal connection.
set showbreak=+         " Show a '+' if a line is longer than the screen.
set linebreak
set display+=lastline
set nostartofline       " Do not jump to first character with page commands,
set number		" show line numbers
set lz			" do not redraw while running macros
set hid			" can change buffer without saving
set backspace=2		" make backspace work normally
set whichwrap+=<,>,h,l  " backspace and cursor keys wrap to
"set mouse=a		" use mouse everywhere
set shortmess=atI	" shortens messages to avoid 'press a key' prompt
set report=0		" tell us when anything is changed via :...
set noerrorbells	" don't make noise
" make the splitters between windows be blank
set fillchars=vert:\ ,stl:\ ,stlnc:\

"-----------------------
" Visual stuff
"-----------------------
set showmatch           " Show matching brackets.
set mat=5		" how many tenths of a second to blink matching brackets
set nohlsearch		" do not highlight search terms
set incsearch           " Incremental search.
set listchars=tab:\|\ ,trail:.,extends:>,precedes:<,eol:$ " what to show when I hit :set list
set textwidth=70        " 70 cols width is very safe.
set so=10		" Keep 10 lines (top/bottom) for scope
set novisualbell	" don't blink
set statusline=%F%m%r%h%w\ %{fugitive#statusline()}\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%04v][%p%%]\ [LEN=%L]
" set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%04v][%p%%]\ [LEN=%L]
" set statusline=%{fugitive#statusline()}
set laststatus=2	" always show the status line
set t_Co=256

colorscheme gruvbox
set background=dark
"colorscheme zellner
"colorscheme distinguished
"colorscheme slate
"colorscheme lumberjack
"
"
"-----------------------
" Text Formatting
"-----------------------
set fo=tcrqn		" See Help (complex)
set autoindent		" Autoindent my code.
set smartindent		" set smart indent
set cindent		" cindent.
"set tabstop=8		" number of spaces of tab character
"set softtabstop=8	" same as above
"set shiftwidth=8	" number of space to (auto)indent
set tabstop=4		" number of spaces of tab character
set softtabstop=4	" same as above
set shiftwidth=4	" number of space to (auto)indent
set noexpandtab		" real tabs only
"set nowrap		" do not wrap lines
set wrap
set linebreak
set nolist		"list disables linebreak
set textwidth=0
set wrapmargin=0
set smarttab		" use tabs at the start of a line, spaces elsewhere

"-------------------------
" Custom Commands
"-------------------------
:command StripTrailing :%s/\s\+$//
:command RemoveHTML    :%s#<[^>]\+>##g

"------------------------
" For orgmode
"------------------------
filetype plugin indent on


"-----------------------
" Folding
"-----------------------
set foldenable		" Turn on folding
set foldmethod=indent	" Make folding indent sensitive
set foldlevel=100	" Don't autofold anything
set foldopen-=search	" don't open folds when you search into them
set foldopen-=undo	" don't open folds when you undo stuff

"------------------------------------
" pathogen
"------------------------------------
execute 	pathogen#infect()
"-------------------------------
" syntastic
"------------------------------
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
"------------------------------------
"	vim-airline
"------------------------------------
let g:airline_section_b = '%{strftime("%c")}'
let g:airline_section_y = 'BN: %{bufnr("%")}'
let g:airline_section_c = '%{fugitive#statusline()}'
let g:airline_theme = 'dark'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = "|"
let g:airline#extensions#tabline#right_sep = "|"
let g:airline#extensions#tabline#buffer_nr_show = 1

"Unicode : 203A
"let g:airline_left_sep = "›"
"Unicode 2039
"let g:airline_right_sep = "‹"

"Powerline
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

python3 from powerline.vim import setup as powerline_setup
python3 powerline_setup()
python3 del powerline_setup


" unicode symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

"airline symbols
"let g:airline_left_sep = ''
"let g:airline_left_alt_sep = ''
"let g:airline_right_sep = ''
"let g:airline_right_alt_sep = ''
"let g:airline_symbols.branch = ''
"let g:airline_symbols.readonly = ''
"let g:airline_symbols.linenr = ''

"let g:airline_theme = 'molokai'
let g:airline_theme = 'gruvbox'

"SimpylFold
let g:SimpylFold_docstring_preview = 1

"python-mode
"let g:pymode = 1
"
"
"------------------------------------
"   Nerd Tree
"------------------------------------
map <C-n> :NERDTreeToggle<CR>
let g:NERDTreeWinSize=60

"------------------------------------
"  Moving between tabs
"------------------------------------
"
"
"------------------------------------
"	VimWiki
"------------------------------------
let wiki = {}
let wiki.path = '~/Documents/wiki/'
let wiki.nested_syntaxes = {'py': 'python', 'ruby': 'ruby'}
let g:vimwiki_list = [wiki]

let g:vimwiki_folding = 'list'


"------------------------------------
"	Start VimWiki Page on start	
"------------------------------------
autocmd VimEnter * if argc() == 0 | execute 'VimwikiIndex' | endif
