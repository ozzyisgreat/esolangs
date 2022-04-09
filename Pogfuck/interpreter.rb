#!/usr/bin/ruby
eval 'm=Hash.new(p=0);'+ARGF.read.gsub(
       /po+g|./,
       'pog'=>'p+=1;',
       'poog'=>'p-=1;',
       'pooog'=>'m[p]+=1;',
       'poooog'=>'m[p]-=1;',
       'pooooog'=>'putc m[p];',
       'poooooog'=>'m[p]=STDIN.getbyte if !STDIN.eof;',
       'pooooooog'=>'(',
       'poooooooog'=>')while((m[p]&=255)!=0);')



