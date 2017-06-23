"显示行数，设置软回车和缩进还有语法
set number
set expandtab
set tabstop=8
set shiftwidth=4
set softtabstop=4
set autoindent
:syntax on
"补全设置
let Tlist_Ctags_Cmd='/usr/bin/ctags'
filetype plugin indent on
filetype plugin on
set ofu=syntaxcomplete#Complete
"一行的字符超出60个就把超出字符的颜色设为红色
highlight OverLength ctermbg=red ctermfg=white guibg=#592929
match OverLength /\%60v.\+/
""this must be first, because it changes other options as a side effect
"set nocompatible
"
""show line numbers
"set number
"
""display "__INSERT__" when entering insert mode
"set showmode
"
""incremental search
"set incsearch
"
""highlight matching search terms
"set hlsearch
"
""set ic means case-insensitive search; noic means case-sensitive
"set noic
"
""allow backspacing over any character insert mode
"set backspace=indent,eol,start
"
""do not wrap lines
"set nowrap
"
""set mouse to work in the console
"set mouse=a
"
""keep 50 lines of command line history
"set history=50
"
""show the cursor position
"set ruler
"
""save a backup file
"set backup
"
""the visual bell flashes the background instead of an audible bell
"set visualbell
"
""set sensible defaults for different types of text files
"au filetype c set cindent tw=79
"au filetype sh set ai et sw=4 sts=4 noexpandtab
"au filetype vim set ai et sw=2 sts=2 noexpandtab
"
""indent new lines to match the current identation
"set autoindent
"
""do not replace tabs with spaces
"set noexpandtab
"
""use tabs at the start of a line, space elsewhere
"set smarttab
"
""show syntax highlighting
""syntax on
"
""show whitespace at the end of a line
""highlight whitespaceEOF ctermbg=blue guibg==blue
""match whitespaceEOF /\s\+$/
